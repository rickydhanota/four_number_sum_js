//Write a function that takes in a non-empty arrayof distinct integers and an integer representing a target sum.The function should find all the quadruplets that add up to the target  sum. and in no particular order. Return an array for each quadruplet found.

function fourNumberSum(arr, targetSum) {
    // Write your code here.
    var allPairSums = {};
    var quadruplets = [];
    for (var i=1; i<arr.length-1; i++){
        for(var j = i+1; j<arr.length; j++){//Looking at the next number from i=0
            var currentSum = arr[i] + arr[j]; //Sum up 
            var difference = targetSum - currentSum; //Subtract by the target to find the difference
            if (difference in allPairSums){//Checking to see if the difference exists in the allPairSums dictionary, and on the first pass it wont exist because there should be nothing in there
                for(var pair of allPairSums[difference]){
                    quadruplets.push(pair.concat( [arr[i], arr[j]] ) );
                }
            }
        }
        for (let k=0; k<i; k++){
            var currentSum = arr[i] + arr[k];
            if(!(currentSum in allPairSums)){
                allPairSums[currentSum] = [ [arr[k], arr[i]] ];
            }
            else{
                allPairSums[currentSum].push([arr[k], arr[i]]);
            }
        }
    }
    return quadruplets;
}
      
console.log(fourNumberSum([7,6,4,-1,1,2], 16));