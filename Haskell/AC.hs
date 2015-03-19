import Text.Printf (printf)

-- This function should return a list [area, volume].
solve :: Int -> Int -> [Int] -> [Int] -> [Double]
solve l r fac expo = 
    let poly = zip fac expo
        xs = [fromIntegral l, 0.001 .. fromIntegral r]
        areaUC = sum $ map (f poly) xs
    in [areaUC]

f :: [(Int,Int)] -> Double -> Double
f poly x = sum $ map (\(fac, expo) -> (fromIntegral fac) * x ^ expo) poly

--Input/Output.
main :: IO ()
main = getContents >>= mapM_ (printf "%.1f\n"). (\[a, b, [l, r]] -> solve l r a b). map (map read. words). lines

