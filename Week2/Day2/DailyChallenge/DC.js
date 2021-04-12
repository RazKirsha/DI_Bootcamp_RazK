let sentence = "The movie is not that bad, I like it";
let final;
let subs;

let wordNot = sentence.search('not');
let wordBad = sentence.search('bad');

if (wordBad > wordNot && wordNot != -1) {
    subs = sentence.substring(wordNot,wordBad+3);
    final = sentence.replace(subs,"good");
} else {
    final = sentence;
}

alert(final)