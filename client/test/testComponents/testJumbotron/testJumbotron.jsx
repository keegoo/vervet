import React from 'react'
import Jumbotron from 'srcDir/components/Jumbotron/Jumbotron.jsx'
import { expect } from 'chai'
import { shallow } from 'enzyme'

describe('<Jumbotron />', () => {

  it('accepts title as props', () => {
    const wrapper = shallow(<Jumbotron title='aTitle'/>)
    expect(wrapper.find('div p').at(0).text()).to.equal('aTitle')
  })

  it('accepts intro as props', () => {
    const wrapper = shallow(<Jumbotron intro='aIntroduction' />)
    expect(wrapper.find('div p').at(1).text()).to.equal('aIntroduction')
  })

  it('use default value if no title props', () => {
    const wrapper = shallow(<Jumbotron />)
    expect(wrapper.find('div p').at(0).text()).to.equal('default title')
  })

  it('use default value if no intro props', () => {
    const wrapper = shallow(<Jumbotron />)
    expect(wrapper.find('div p').at(1).text()).to.equal('default introduction')
  })

  it('should render its child element', () => {
    const wrapper = shallow(
      <Jumbotron>
        <button>click</button>
      </Jumbotron>
    )
    expect(wrapper.contains(<button>click</button>)).to.equal(true)
  })
})
