import React from 'react'
import Jumbotron from 'srcDir/components/Jumbotron/Jumbotron.jsx'
import { expect } from 'chai'
import { shallow } from 'enzyme'

describe('<Jumbotron />', () => {
  const wrapperA = shallow(
    <Jumbotron 
      title='aTitle'
      intro='aIntroduction' />
  )

  it('accepts title as props', () => {
    expect(wrapperA.find('div p').at(0).text()).to.equal('aTitle')
  })

  it('accepts intro as props', () => {
    expect(wrapperA.find('div p').at(1).text()).to.equal('aIntroduction')
  })

  const wrapperB = shallow(
    <Jumbotron />
  )
  it('use default value if no title props', () => {
    expect(wrapperB.find('div p').at(0).text()).to.equal('default title')
  })

  it('use default value if no intro props', () => {
    expect(wrapperB.find('div p').at(1).text()).to.equal('default introduction')
  })

  const wrapperC = shallow(
    <Jumbotron>
      <button>click</button>
    </Jumbotron>
  )

  it('should render its child element', () => {
    
  })
})
