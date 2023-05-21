import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {HashRouter} from "react-router-dom";

const root = ReactDOM.createRoot(
    document.getElementById('root') as HTMLElement
);

export type DialogType = {
    id: number
    name: string
}
export type MessageType = {
    id: number
    message: string
}
export type PostType = {
    id: number
    text: string
    likesCount: number
}

const dialogsData: DialogType[] = [
    {id: 1, name: 'Kirill'},
    {id: 2, name: 'Tayson'},
    {id: 3, name: 'Anya'},
]

const messagesData: MessageType[] = [
    {id: 1, message: '159'},
    {id: 2, message: '1jhjh59'},
    {id: 3, message: '4654oip'},
]

const postsData: PostType[] = [
    {id: 1, text: 'kirill', likesCount: 12},
    {id: 2, text: 'Anya', likesCount: 10},
    {id: 3, text: 'Tayson', likesCount: 8},
]

root.render(
    <HashRouter>
        <App
            dialogs={dialogsData}
            messages={messagesData}
            posts={postsData}
        />
    </HashRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
