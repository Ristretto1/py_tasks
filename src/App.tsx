import React from 'react';
import './App.css';

function App() {
    return (
        <div className="app_wrapper">
            <header className="header">Header</header>
            <div className="main_wrapper">
                <nav className="nav">
                    <ul>
                        <li><a href="#">Profile</a></li>
                        <li><a href="#">Messages</a></li>
                        <li><a href="#">News</a></li>
                        <li><a href="#">Music</a></li>
                        <li><a href="#">Settings</a></li>
                    </ul>
                </nav>
                <main className="content">content</main>
            </div>
        </div>
    );
}

export default App;
