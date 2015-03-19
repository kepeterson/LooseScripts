import Data.List

main = do
    input <- getContents
    let inpLines = lines input
    let array = map read (words $ (inpLines) !! 1) :: [Integer]
    let queries = (tail . tail . tail) inpLines
    let tuples = map (\[a,b] -> (read a, read b)) (map words queries)
    let results = map (query array) tuples
    putStrLn(show tuples)
    
query :: [Integer] -> (Integer,Integer) -> Integer
query array (idx, margin) = 
    let (hd, tl) = genericSplitAt (idx + 1) array
        lessThanFirst = takeWhile (\a -> (a >(last hd)) && (a < (last hd + margin))) tl
        otherList = takeWhile (\a -> (a>(last hd)) && (a<(last hd + margin))) (reverse hd)
    in genericLength lessThanFirst + genericLength otherList
