import React from 'react';
import {NavLink} from "react-router-dom";
import {Dialog} from "./Dialog/Dialog";
import {Message} from "./Message/Message";

export const Dialogs = () => {

    const styleDialogsWrapper = {
        display: 'flex'
    }
    const styleDialogs = {
        width: '150px'
    }

    const dialogsData = [
        {id: 1, name: 'Kirill'},
        {id: 2, name: 'Tayson'},
        {id: 3, name: 'Anya'},
    ]
    const messagesData = [
        {id: 1, message: '159'},
        {id: 2, message: '1jhjh59'},
        {id: 3, message: '4654oip'},
    ]


    return (
        <div className={'dialogs_wrapper'} style={styleDialogsWrapper}>
            <div className={'dialogs'} style={styleDialogs}>
                {dialogsData.map(el => <Dialog name={el.name} id={el.id} key={el.id}/>)}

            </div>
            <div className="messages">
                {messagesData.map(el => <Message message={el.message} key={el.id}/>)}
            </div>
        </div>
    );
};

