function isPalindrome(sen){
    woSpace = sen.replace(/\s/g,"");
    woSpace = woSpace.toLowerCase();
    let backward = '';
    for (let i = woSpace.length-1; i >=0 ; i--) {
        backward += woSpace[i];
    }
    if (woSpace == backward){
        console.log(true);
    }else {
        console.log(false);
    }
}

isPalindrome("Aba");