var fs = require('fs')
var path = require('path')

var srcFile = fs.readFileSync(path.resolve('../', 'text.txt'))
var srcFileWords = srcFile.toString().split(' ') // assume we cound get correct words by this way
var wordMap = {}
var finalText = ''

// count and collection them to a Object/Map/Dict
srcFileWords.forEach(function(word){
  if (!wordMap[word])
    wordMap[word] = 0

  wordMap[word] ++
})

// That's do this:
finalText = Object.keys(wordMap)
  // Create a Array with word itself and it's count
  .map(function(word){
    return {
      word: word,
      count: wordMap[word]
    }
  })
  // Sort by object.count( words number)
  .sort(function(a, b){
    return a.count < b.count
  })
  // Create a string that what we wanted
  .map(function(item){
    return item.word + ' shows ' + item.count + ' times'
  }).join('\n')

// Write that result to disk:
fs.writeFileSync('output.csv', finalText)