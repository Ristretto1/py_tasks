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


    return (
        <div className={'dialogs_wrapper'} style={styleDialogsWrapper}>
            <div className={'dialogs'} style={styleDialogs}>
                <Dialog name={'Kirill'} id={1}/>
                <Dialog name={'Tayson'} id={2}/>
                <Dialog name={'Anya'} id={3}/>
            </div>
            <div className="messages">
                <Message message={'159'}/>
                <Message message={'1jhjh59'}/>
                <Message message={'4654oip'}/>
                <Message message={'236'}/>
            </div>
        </div>
    );
};

