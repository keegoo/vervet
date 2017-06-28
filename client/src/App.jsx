import React from 'react'
import ReactDOM from 'react-dom'
import Jumbotron from './components/Jumbotron/Jumbotron.jsx'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'

class App extends React.Component {
  render(){
    return(
      <div>
        <h1>React APP!</h1>
        <Jumbotron />
      </div>
    )
  }
}

ReactDOM.render((
  <MuiThemeProvider>
    <App />
  </MuiThemeProvider>
  ), 
  document.getElementById("main")
)