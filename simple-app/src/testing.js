import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import './index.css'

function getCurrentDate() {

  let newDate = new Date()
  let date = newDate.getDate();
  let month = newDate.getMonth() + 1;
  let year = newDate.getFullYear();

  return <h1>{date} {month} {year}</h1>
}

console.log(getCurrentDate);

// THOSE 3 DO EXACTLY THE SAME THING!!!
// const element = (
//   <h1 className="greeting">
//     Hello, world!
//   </h1>
// );

// const element = React.createElement(
//   'h1',
//   {className: 'greeting'},
//   'Hello, world!'
// );

// const element = {
//   type: 'h1',
//   props: {
//     className: 'greeting',
//     children: 'Hello, world!'
//   }
// };

const name = "Mario Schwabe"
const element = <h1>Hello {name}</h1>;

function formatName(user) {
  return user.firstName + ' ' + user.lastName;
}

const user = {
  firstName: "Mario",
  lastName: "Schwabe"
};


const newUser = (
  <h1>
    Hi there {formatName(user)}!
  </h1>
)

function getGreeting(user) {
  if (user) {
    return <h1>
      hello {formatName(user)}
    </h1>
  }
  return <h1>We don´t know you!</h1>
}

class App extends Component {
  render() {
    return (
      <div className="app">
        {element}
        {newUser}
        {getGreeting(user)}
        {getCurrentDate()}
      </div>
    )
  }
}

ReactDOM.render(<App />, document.getElementById('root'))