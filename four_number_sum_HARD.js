//Write a function that takes in a non-empty arrayof distinct integers and an integer representing a target sum.The function should find all the quadruplets that add up to the target  sum. and in no particular order. Return an array for each quadruplet found.

function fourNumberSum(arr, targetSum) {
    // Write your code here.
      var allPairSums = {};
      var quadruplets = [];
      for (var i=1; i<arr.length-1; i++){
          for(var j = i+1; j<arr.length; j++){
              var currentSum = arr[i] + arr[j];
              var difference = targetSum - currentSum;
              if (difference in allPairSums){
                  for(var pair of allPairSums[difference]){
                      quadruplets.push(pair.concat([arr[i], arr[j]]));
                    }
                }
            }
        for (let k=0; k<i; k++){
            var currentSum = arr[i] + arr[k];
            if(!(currentSum in allPairSums)){
                allPairSums[currentSum] = [[arr[k], arr[i]]];
            }
            else{
                allPairSums[currentSum].push([arr[k], arr[i]]);
            }
        }
    }
    return quadruplets;
}
      
console.log(fourNumberSum([7,6,4,-1,1,2], 16));