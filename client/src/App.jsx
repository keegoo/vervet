import React from 'react'
import ReactDOM from 'react-dom'
import Jumbotron from './components/Jumbotron/Jumbotron.jsx'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'

class App extends React.Component {
  render(){
    return(
      <div style={{width: '60%', margin: 'auto'}}>
        <Jumbotron title="Jumbotron" intro="Here's introduction">
          <button>click</button>
        </Jumbotron>
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