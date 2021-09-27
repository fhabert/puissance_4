const initGame = () => {
    const posDir = availablePos();
    const dic1 = JSON.parse(document.getElementById('dic1').innerText);
    const dic2 = JSON.parse(document.getElementById('dic2').innerText);
    let idStrings1 = [];
    let idStrings2 = [];
    let str = '';

    for (let i = 0; i < dic1.length - 1; i += 2) {
        idStrings1.push(`${dic1[i]}${dic1[i+1]}`);
        str = '';
    }
    for (let i = 0; i < dic2.length - 1; i += 2) {
        idStrings2.push(`${dic2[i]}${dic2[i+1]}`);
        str = '';
    }
    let idStrings = [];
    posDir.forEach((ar) => {
        ar.forEach((el) => {
            idStrings.push(el.join(''));
        })
    });
    idStrings1.forEach((el) => {
        let text = `square-${el}`;
        const square = document.getElementById(text);
        square.children[0].firstChild.classList.add('piece_rouge');
    })
    idStrings2.forEach((el) => {
        let text = `square-${el}`;
        const square = document.getElementById(text);
        square.children[0].firstChild.classList.add('piece_bleue');
    })
    idStrings.forEach((el) => {
        let text = `square-${el}`;
        const square = document.getElementById(text);
        square.classList.add('yellow-square');
    })
}

const availablePos = () => {
    const posDirsElement = document.querySelector('#posDirHTML');
    const posDirs = JSON.parse('[' + posDirsElement.innerText + ']');
    const idString = [];
    posDirs.forEach((ar) => {
        ar.forEach((el) => {
            idString.push(el.join(''));
        })
    })
    return posDirs;
}

const personPos = () => {
    const posPerson = document.querySelector('#posDirPersonHtml').innerHTML;
    console.log(JSON.stringify(posPerson));
}

initGame();





// square.addEventListener('click', (e) => {
//     check = !check;
//     if (check) {
//         square.classList.remove('yellow-square');
//         square.children[0].classList.add('piece_rouge');
//     } else {
//         square.classList.remove('yellow-square');
//         square.children[0].classList.add('piece_bleue');
//     }
//     const idSquare = e.currentTarget.attributes.id.value.split('-')[1];
//     let index = 0;
//     for (let i = 0; i < idStrings.length; i++) {
//         if (idStrings[i] === idSquare) {
//             index = i;
//         }
//     }
// })
// const postAPI = (posDir) => {
//     const jsonPosDir = JSON.stringify(posDir);
//     fetch(`http://localhost:5000/json/${posDir}`, {
//         method: 'POST',
//         mode: 'no-cors',
//         header: "Content-Type: application/json",
//         contentType: 'application/json',
//         dataType: 'json',
//         data: { "possibleDir": jsonPosDir } 
//     })
// }


