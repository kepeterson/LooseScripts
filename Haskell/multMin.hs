import qualified Data.Sequence as S
import qualified Data.Foldable as F
import Control.Monad

main = do
    input <- readFile "test.txt"
    let array = map read (words $ (lines input) !! 1) :: [Integer]
    let tasks = tail . tail . tail $ lines input
    let results = controller2 array tasks
    putStrLn(unlines results)
    
controller2 :: [Integer] -> [String] -> [String]
controller2 _ [] = []
controller2 array (task:xs) =
    let taskArr = words task
        func = if head taskArr == "Q"
            then query array (read (taskArr !! 1)) (read (taskArr !! 2))
            else update' array (read (taskArr !! 1)) (read (taskArr !! 2))
        func2 = if (length func) > 1
            then controller2 func xs
            else (show (head func)): controller2 array xs
    in func2
 
{--
controller :: [Int] -> String -> IO ()
controller array str =
    let task = words str
        func = if head task == "Q"
            then query array (read (task !! 1)) (read (task !! 2))
            else return ()--update' array (read (task !! 1)) (read (task !! 2))
    in func--}

query :: [Integer] -> Int -> Int -> [Integer]
query ls index1 index2 = 
    let choppedLst = take (index2 - index1 + 1) $ drop index1 ls
    in [mod (foldr (\x acc -> lcm x acc) (1 :: Integer) choppedLst) (10 ^ 9 + 7)]
    
update' :: [Integer] -> Int -> Int -> [Integer]
update' lsx index multi = 
    let ls = map fromIntegral lsx 
    in map toInteger $ F.toList $ S.update index (multi * (ls !! index)) $ S.fromList ls