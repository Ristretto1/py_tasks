import React from 'react';
import './App.css';
import {Header} from "./components/Header/Header";
import {Navbar} from "./components/Navbar/Navbar";
import {Profile} from "./components/Profile/Profile";
import {Dialogs} from "./components/Dialogs/Dialogs";
import {Route, Routes} from "react-router-dom";
import {Music} from "./components/Music/Music";
import {News} from "./components/News/News";
import {Settings} from "./components/Settings/Settings";
import {DialogType, MessageType, PostType} from "./index";

type AppPropsType = {
    dialogs: DialogType[]
    messages: MessageType[]
    posts: PostType[]
}
function App(props: AppPropsType) {
    return (
        <div className="app_wrapper">
            <Header/>
            <div className="main_wrapper">
                <Navbar/>
                <div className={'content'}>
                    <Routes>
                        <Route element={<Profile posts={props.posts}/>} path={'/profile'}/>
                        <Route element={<Dialogs messages={props.messages} dialogs={props.dialogs}/>} path={'/dialogs'}/>
                        <Route element={<News/>} path={'/news'}/>
                        <Route element={<Music/>} path={'/music'}/>
                        <Route element={<Settings/>} path={'/settings'}/>
                    </Routes>
                </div>
            </div>
        </div>
    );
}

export default App;
