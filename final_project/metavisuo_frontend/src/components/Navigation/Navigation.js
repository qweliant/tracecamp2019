import React from 'react';
import { Navbar, NavbarBrand  } from "shards-react";



const navBg = {
    backgroundColor: '#abb4fe',
};

const navFont = {
    fontSize: '20px',
};

const Navigation = () => {
    return ( 
        <Navbar type="dark" expand="md" style ={navBg} >
            <NavbarBrand href="#" style={navFont}>Trainamodel</NavbarBrand>
        </Navbar> 
    );
}

export default Navigation;