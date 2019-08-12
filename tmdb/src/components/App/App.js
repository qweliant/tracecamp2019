import React from 'react';
import Movie from '../Movie/Movie';
import MoviePicker from '../MoviePicker/MoviePicker';
import Movies from '../Movies/Movies';
import ResponsiveDrawer from '../Navigate/Navigate';
import HomePage from '../Home/Home'
import UpdatePage from '../Update/Update'
import CreatePage from '../Create/Create'
import DetailPage from '../Detail/Detail'
import ListPage from '../List/List'
import {BrowserRouter as Router, NavLink, Route, Link} from 'react-router-dom';


const pages=[
    {
      component: HomePage,
      path: "/Home",
      to:"Home"
    }, 
    {
      component: CreatePage,
      path: "/Create",
      to: "Create"
    },
    {
      component: ListPage,
      path: "/List",
      to: "List"
    }
  ]
  



const App=()=>{
    return (
        <div>    
            <Router>
                <ResponsiveDrawer/>
            </Router>
        </div>
    );
}

export default App;