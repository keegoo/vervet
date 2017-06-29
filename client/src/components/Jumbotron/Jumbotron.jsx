import React from 'react'
import PropTypes from 'prop-types'
import theme from '../styles/theme.js'

const getStyles = () => {
  const {spacing, size, palette} = theme

  return {
    paper: {
      backgroundColor: palette.primary1Color,
      padding: spacing.desktopGutter
    },
    title: {
      fontSize: size.large
    },
    paragraph: {
      fontSize: size.normal
    }
  }
}

const Jumbotron = (props) => {
  const styles = getStyles()
  const title = props.title || 'default title'
  const intro = props.intro || 'default introduction'

  return(
    <div style={styles.paper}>
      <p style={styles.title}>{title}</p>
      <p style={styles.paragraph}>{intro}</p>
      {props.children}
    </div>
  )
}

Jumbotron.propTypes = {
  title: PropTypes.string.isRequired,
  intro: PropTypes.string.isRequired
} 

export default Jumbotron