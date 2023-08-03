// Code 1
//window.addEventListener('load', () => {
//  fetch('https://example.com/api/title') // Replace with your API endpoint
//     .then(response => response.json())
//     .then(data => {
//       const titleElement = document.getElementById('banner-title');
//       titleElement.textContent = data.title;
//     })
//     .catch(error => {
//       console.error('Error fetching title:', error);
//     });
// });

// Code 2
//const titleElement = document.getElementById('banner-title');
// let titleIndex = 0;
// const titles = ['Title 1', 'Title 2'];
//
// function changeTitle() {
//   titleIndex = (titleIndex + 1) % titles.length;
//   titleElement.textContent = titles[titleIndex];
// }

//Code 3
// function changeTitle() {
//     fetch('http://127.0.0.1:5000/api/title')
//         .then(response => response.json())
//         .then(data => {
//             const titleElement = document.getElementById('banner-title');
//             titleElement.textContent = data.title;
//         })
//         .catch(error => {
//             console.error('Error fetching title:', error);
//         });
// }

function fetchData() {
    fetch('http://localhost:8080/api/data')
    .then(response => response.json())
    .then(data => {
        // Update title in the banner
        const titleElement = document.getElementById('banner-title');
        titleElement.textContent = data.title;

        // Update number in quadrant 1
        const number1Element = document.getElementById('number1');
        number1Element.textContent = data.number;

        // Update text in quadrant 1
        const text1Element = document.getElementById('text1');
        fetch(data.text_path)
            .then(response => response.text())
            .then(text => {
                text1Element.textContent = text;
            })
            .catch(error => {
                console.error('Error fetching text:', error);
            });

        // Update image in quadrant 1
        const image1Element = document.getElementById('image1');
        image1Element.src = data.image_path;
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
}
