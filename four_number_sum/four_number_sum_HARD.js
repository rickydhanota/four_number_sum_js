//Write a function that takes in a non-empty arrayof distinct integers and an integer representing a target sum.The function should find all the quadruplets that add up to the target  sum. and in no particular order. Return an array for each quadruplet found.

function fourNumberSum(arr, targetSum) {
    // Write your code here.
    var allPairSums = {}; //Creating an object
    var quadruplets = [];
    for (var i=1; i<arr.length-1; i++){// we can start at the second value because at the first value theres nothing in our javascript object, and we can skip the last value because there is nothing that comes after the last value
        for(var j = i+1; j<arr.length; j++){//Looking at the next number from i
            var currentSum = arr[i] + arr[j]; //Sum up 
            var difference = targetSum - currentSum; //Subtract by the target to find the difference
            if (difference in allPairSums){//Checking to see if the difference exists in the allPairSums dictionary, and on the first pass it wont exist because there should be nothing in there
                for(var pair of allPairSums[difference]){// the of operator allows us to iterate over an object
                    quadruplets.push(pair.concat( [arr[i], arr[j]] ) );//.concat merges 2 arrays
                }
            }
        }
        for (let k=0; k<i; k++){
            var currentSum = arr[i] + arr[k];
            if(!(currentSum in allPairSums)){
                allPairSums[currentSum] = [ [arr[k], arr[i]] ]; //Creates a key value pair, by first creating the key "currentSum" and assigning it a value of [ [arr[k], arr[i]] ]
            }
            else{
                allPairSums[currentSum].push([arr[k], arr[i]]);
                // console.log("all pairs", allPairSums); if we have duplicates it pushes
            }
        }
    }
    return quadruplets;
}
      
console.log(fourNumberSum([7,6,4,-1,1,2], 16));

