import UIKit

func countPathsBacktrackingOptimized(_ steps: Int) -> Int {
    var arr = [Int](repeating: 0, count: steps)
    arr[0] = 1
    var count = 0
    var leapTotal = 1
    var i = 0
    
    while true {
//        print(arr)
        iterations += 1
        // Move forward if leapTotal < steps
        if leapTotal < steps {
            i += 1
            arr[i] = 1
            leapTotal += 1
        }
        
        if leapTotal == steps {
//            print(arr)
            count += 1
            // remove arr[i] from leap total
            leapTotal -= arr[i]
            // reset arr[i] value
            arr[i] = 0
            // move back one index
            i -= 1
            // increase the value by 1
            arr[i] += 1
            // increase the total by one
            leapTotal += 1
        }
        
        if leapTotal > steps || arr[i] > 3 {
//            print ("greater\t", arr)
            // Exit check
            if i == 0 {
                return count
            }
            while leapTotal > steps || arr[i] > 3 {
//                print(i, "      ", arr)
                if i == 0 && arr[i] > 3 {
                    return count
                }
                
                leapTotal -= arr[i]
                arr[i] = 0
                i -= 1
                arr[i] += 1
                leapTotal += 1
            }
        }
    }
    return count
}

func countPathsBacktracking(_ steps: Int) -> Int {
    var arr = [Int](repeating: 0, count: steps)
    arr[0] = 1
    var count = 0
    var leapTotal = 1
    var i = 0
    
    while true {
        iterations += 1
        //    print(i, arr, leapTotal)
        // Exit check
        if i == 0 && arr[i] > 3 {
            break
        }
        // Backtrack check
        else if arr[i] > 3 ||  leapTotal > steps {
            leapTotal -= arr[i]
            arr[i] = 0
            i -= 1
            
            arr[i] += 1
            leapTotal += 1
        }

        // Print/Count Check
        else if leapTotal == steps {
            print(arr)
            count += 1
            leapTotal -= arr[i]
            arr[i] = 0
            i -= 1
            arr[i] += 1
            leapTotal += 1
        }
        // Move forward if leapTotal < steps
        else if leapTotal < steps {
            i += 1
            arr[i] = 1
            leapTotal += 1
        }
    }
    return count
}

func countPathsRecursive(_ steps: Int) -> Int {
    iterations += 1
    if steps < 0 {
        return 0
    }
    if steps == 0 {
        return 1
    }
    return countPathsRecursive(steps - 1) + countPathsRecursive(steps - 2) + countPathsRecursive(steps - 3)
}

func countPathsMemorization(_ steps: Int) -> Int {
    iterations += 1
    if steps < 0 {
        return 0
    }
    if steps == 0 {
        return 1
    }
    if arr[steps] == 0 {
        arr[steps] = countPathsMemorization(steps - 1) + countPathsMemorization(steps - 2) + countPathsMemorization(steps - 3)
    }
    return arr[steps]
}

func countPathsDynamic(_ steps: Int) -> Int {
    if steps < 0 {
        return 0
    }
    if steps <= 1 {
        return 1
    }
    var arr = [Int](repeating: 0, count: steps + 1)
    arr[0] = 1
    arr[1] = 1
    arr[2] = 2
    
    for i in 3...steps {
        iterations += 1
        arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
    }
    return arr[steps]
}

func countPathsIteritively(_ steps: Int) -> Int {
    if steps < 0 {
        return 0
    }
    if steps <= 1 {
        return 1
    }
    var arr = [1, 1, 2]
    
    for i in 3...steps {
        iterations += 1
        let count = arr[0] + arr[1] + arr[2]
        arr[0] = arr[1]
        arr[1] = arr[2]
        arr[2] = count
     }
    return arr[2]
}

//MARK: - Testing

var iterations = 0
var steps = 10

print("countPathsBacktracking paths:", countPathsBacktracking(steps))
print("countPathsBacktracking iterations: ", iterations)
print("\n")

iterations = 0
print("countPathsBacktrackingOptimized paths:", countPathsBacktrackingOptimized(steps))
print("countPathsBacktrackingOptimized iterations: ", iterations)
print("\n")

iterations = 0
print("countPathsRecursive paths:", countPathsRecursive(steps))
print("countPathsRecursive calls: ", iterations)
print("\n")

iterations = 0
var arr = [Int](repeating: 0, count: steps + 1)
print("countPathsRecursiveMemorization paths:", countPathsMemorization(steps))
print("countPathsRecursiveMemorization calls: ", iterations)
print("\n")

iterations = 0
print("countPathsDynamic paths:", countPathsDynamic(steps))
print("countPathsDynamic iterations: ", iterations)
print("\n")

iterations = 0
print("countPathsIteritive paths:", countPathsIteritively(steps))
print("countPathsIteritive iterations: ", iterations)
print("\n")
