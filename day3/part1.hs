import Data.Char (digitToInt)

parse :: String -> [String]
parse = lines

solve :: [String] -> Int
solve = sum . map solve' where
    
    solve' :: String -> Int
    solve' (a:b:bank) = a' * 10 + b' where
        (a1, b1) = foldl go (a, b) bank
        go (a, b) c
            | a < b     = (b, c)
            | b < c     = (a, c)
            | otherwise = (a, b)
        a' = digitToInt a1
        b' = digitToInt b1

main :: IO ()
main = interact (show . solve . parse)