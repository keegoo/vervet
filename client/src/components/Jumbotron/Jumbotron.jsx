import React from 'react'
import PropTypes from 'prop-types'
import Paper from 'material-ui/Paper'
import theme from '../styles/theme.js'

const getStyles = () => {
  const {spacing, size, palette} = theme

  return {
    paper: {
      backgroundColor: palette.primary1Color,
      padding: spacing.desktopGutter
    },
    heading: {
      fontSize: size.large
    },
    paragraph: {
      fontSize: size.normal
    }
  }
}

const Jumbotron = (props) => {
  const styles = getStyles()

  return(
    <Paper zDepth={1} style={styles.paper}>
      <h1 style={styles.heading}>Vervet monitoring</h1>
      <p style={styles.paragraph}>This is a demo</p>
      <button>Click</button>
    </Paper>
  )
} 

export default Jumbotron