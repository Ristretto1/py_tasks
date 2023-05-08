import React from 'react';
import './App.css';
import {Header} from "./components/Header";
import {Navbar} from "./components/Navbar";
import {Profile} from "./components/Profile";

function App() {
    return (
        <div className="app_wrapper">
            <Header/>
            <div className="main_wrapper">
                <Navbar/>
                <Profile/>
            </div>
        </div>
    );
}

export default App;
