
```js
function bsearch(arr,target, l, r){
  if(arr[r] < target || arr[l] > target) return arr;
  
  let m = Math.floor((l+r)/2);
  let value = arr[m];
  
  if(r-l < 2){
    if(arr[l] === target) arr = [...arr.slice(0,l),...arr.slice(l+1,arr.length)];
    if(arr[r] === target && r !== l) arr = [...arr.slice(0,r),...arr.slice(r+1,arr.length)];
    return arr;
  }

  if(target < value){
    return bsearch(arr,target,l,m-1);
  }else if (target > value){
    return bsearch(arr,target,m+1,r);
  }else if(target === value){
    arr = [...arr.slice(0,m),...arr.slice(m+1,arr.length)];
    r = arr.length-1;
    m = Math.floor((l+r)/2);
    return bsearch(bsearch(arr,target,l,m-1),target,m+1,r);
  }
}

let arr = [1,2]
let targets = [3,5];

for(const target of targets){
  arr = bsearch(arr,target,0,arr.length-1);
}
  console.log(arr);
```

