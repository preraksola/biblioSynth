import System.Environment


build_command li field inter = 
    let (x:xs) = map (\x -> "\"" ++ x ++ "\"" ++ field) li in
        foldl (\a b -> a ++ inter ++ b) x xs

main = do
    file:field:inter:args <- getArgs
    contents <- readFile file
    putStrLn $ build_command (lines contents) field inter
