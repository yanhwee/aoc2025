import Data.List (unfoldr, splitAt)
import Data.Bool (bool)
import Data.Maybe (fromMaybe)

safeTail :: [a] -> Maybe [a]
safeTail = (bool Nothing . (Just . tail)) <*> (not . null)

splitOn :: Eq a => a -> [a] -> [[a]]
splitOn c = unfoldr go where
    go s = if null s then Nothing else Just $ split s
    split s = fromMaybe [] . safeTail <$> break (== c) s

parse :: String -> [(Int, Int)]
parse = map parse' . splitOn ',' where
    parse' line = case splitOn '-' line of
        [a, b] -> (read a, read b)
        _ -> undefined

isInvalid :: Int -> Bool
isInvalid num = match where
    s = show num
    n = length s
    ixs = [1..(n `div` 2)]
    isDiv a b = a `mod` b == 0
    jxs = filter (n `isDiv`) ixs
    rep i = concat $ replicate (n `div` i) (take i s)
    match = any ((s ==) . rep) jxs

solve :: [(Int, Int)] -> Int
solve = sum . filter isInvalid . nums where
    enumFromTo' = uncurry enumFromTo
    nums = concatMap enumFromTo'

main :: IO ()
main = interact (show . solve . parse)