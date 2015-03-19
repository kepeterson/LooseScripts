import Data.Char
import qualified Data.Sequence as S
import qualified Data.Foldable as F

data Factor = Factor {prime :: Int, expo :: Int} deriving (Show)
type Factors = [Factor]

-- Enter your code here. Read input from STDIN. Print output to STDOUT
main = do
    input <- getContents
    let z = map parse (map words (tail $ lines input))
    putStrLn (show z)
    
parse :: [String] -> Factors
parse [] = []
parse (x:y:xs) = Factor (read x) (read y) : parse xs

{--
--takes a list of factors (the current GCD)
--and then sees if its in the other list of factors
gcd' :: Factors -> Factors -> Factors
gcd' [] _ = []
gcd' (a:as) b = (factorElem a b) : (gcd' as b)
--}

factorElem :: Factor -> Factors -> Factors
factorElem _ [] = []
factorElem (Factor primex expot) (a:as)
    | primex == prime a = Factor primex (min expot (expo a)) : factorElem (Factor primex expot) as
    | otherwise = factorElem (Factor primex expot) as
    
query :: [Int] -> Int -> Int -> Int
query ls index1 index2 = 
    let choppedLst = take (index2 - index1 + 1) $ drop index1 ls
    in foldr (\x acc -> lcm x acc) 1 choppedLst
    
update' :: [Int] -> Int -> Int -> [Int]
update' ls index multi = F.toList $ S.update index (multi * ls !! index) $ S.fromList ls
