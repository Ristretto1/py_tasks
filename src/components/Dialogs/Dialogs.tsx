import React from 'react';
import {NavLink} from "react-router-dom";

export const Dialogs = () => {

    const styleDialogsWrapper = {
        display: 'flex'
    }
    const styleDialogs = {
        width: '150px'
    }
    const styleDialogsActive = {
        color: 'white'
    }
    const styleDialogsItem = {
        padding: '5px'
    }
    const styleMessagesItem = {
        padding: '5px'
    }

    return (
        <div className={'dialogs_wrapper'} style={styleDialogsWrapper}>
            <div className={'dialogs'} style={styleDialogs}>
                <div className={'dialogs_item'} style={styleDialogsItem}>
                    <NavLink to={'/dialogs/'}>Kirill</NavLink>
                </div>
                <div className={'dialogs_item'} style={{...styleDialogsItem, ...styleDialogsActive}}>
                    <NavLink to={'/dialogs/'}>Tayson</NavLink>
                </div>
                <div className={'dialogs_item'} style={styleDialogsItem}>
                    <NavLink to={'/dialogs/'}>Anya</NavLink>
                </div>
            </div>
            <div className="messages">
                <div className="messages_item" style={styleMessagesItem}>123</div>
                <div className="messages_item" style={styleMessagesItem}>456</div>
                <div className="messages_item" style={styleMessagesItem}>789</div>
                <div className="messages_item" style={styleMessagesItem}>789</div>
                <div className="messages_item" style={styleMessagesItem}>789</div>
            </div>
        </div>
    );
};

