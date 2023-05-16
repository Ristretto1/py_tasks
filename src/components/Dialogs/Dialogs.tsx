import React from 'react';

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
                <div className={'dialogs_item'} style={styleDialogsItem}>Kirill</div>
                <div className={'dialogs_item'} style={{...styleDialogsItem, ...styleDialogsActive}}>Tayson</div>
                <div className={'dialogs_item'} style={styleDialogsItem}>Anya</div>
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

