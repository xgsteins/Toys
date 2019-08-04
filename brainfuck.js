function check(str) {
    var bracket = []
    var char = ['+', '-', '>', '<', '[', ']', ',', '.']
    for (let index = 0; index < str.length; index++) {
        const element = str[index]
        if (char.includes(element) == false) {
            return false
        }
        if (element == '[') {
            bracket.push(element)
        } else if (element == ']') {
            if (bracket.length == 0) {
                return false
            }
            bracket.pop()
        }
    }
    if (bracket.length == 0) {
        return true
    } else {
        return false
    }
}

function parser(str) {
    var memory = []
    var output = []
    var bracketpos = []
    var pos = 0
    var index = 0
    while (index < str.length) {
        // setTimeout(() => {
            switch (str[index]) {
                case '>':
                    pos++
                    break
                case '<':
                    pos--
                    break
                case '+':
                    if (memory[pos] == undefined) {
                        memory[pos] = 0
                    }
                    memory[pos]++
                    break
                case '-':
                    if (memory[pos] == undefined) {
                        memory[pos] = 0
                    }
                    memory[pos]--
                    break
                case '.':
                    output.push(String.fromCharCode(memory[pos]))
                    break
                case ',':
                    // 咕咕咕
                    break
                case '[':
                    if (memory[pos] == undefined || memory[pos] == 0) {
                        memory[pos] = 0
                        while (index < str.length && str[index] != ']') {
                            index++
                        }
                    } else {
                        bracketpos.push(index)
                    }
                    break
                case ']':
                    if (memory[pos] != 0) {
                        index = bracketpos[bracketpos.length-1]
                    } else {
                        bracketpos.pop()
                    }
                    break
                default:
                    break
            }
        // }, 1)
        index++
    }
    alert(output.join(''))
}
// ++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.