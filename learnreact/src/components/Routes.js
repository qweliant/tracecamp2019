import React from "react";
import {BrowserRouter, Route, Link } from "react-router-dom";
import Blog from "./Blog"
import HomeView from "./Home"

function Home(){
    return <HomeView/>
}

function Post(){
    return <h1>Memories Don't Die <Blog/></h1>
}

function Projects(){
    return <h1>Projects</h1>
}

function Routing(){
    return(
        <BrowserRouter>
        <div>
            <nav>
                <Link to="/">Home / </Link>
                <Link to="/post">Post / </Link>
                <Link to="/projects">Projects</Link>
            </nav>

            <Route exact path="/" component={Home}></Route>
            <Route path="/post/" component={Post}></Route>
            <Route path="/projects/" component={Projects}></Route>
        </div>
        </BrowserRouter>
    );
}


export default Routing;