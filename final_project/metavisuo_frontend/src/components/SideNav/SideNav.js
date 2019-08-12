import React from 'react';
import { Col, Nav, NavItem, NavLink } from "shards-react";

const navBg = {
    backgroundColor: '#ffE68f',
    fontColor: 'black',
    maxWidth: '15%',
    marginLeft: '-1%'
};

const SideNav = () => {
    return ( 
            <Col>
            <Nav style={navBg}>
                <Col>
                    <NavItem>
                        <NavLink active href="#">
                        Active
                        </NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink href="#">Link</NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink href="#">Another Link</NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink disabled href="#">
                        Disabled Link
                        </NavLink>
                    </NavItem>
                </Col>
            </Nav>
            </Col>
            
    );
}

export default SideNav