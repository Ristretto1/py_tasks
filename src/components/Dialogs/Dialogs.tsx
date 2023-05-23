import React from 'react';
import {Dialog} from "./Dialog/Dialog";
import {Message} from "./Message/Message";
import {DialogType, MessageType} from "../../types";

type DialogsPropsType = {
    messagesData: {
        dialogs: DialogType[]
        messages: MessageType[]
    }
}

export const Dialogs = (props: DialogsPropsType) => {

    const styleDialogsWrapper = {
        display: 'flex'
    }
    const styleDialogs = {
        width: '150px'
    }

    const mappedDialogs = props.messagesData.dialogs.map(el => <Dialog name={el.name} id={el.id} key={el.id}/>)
    const mappedMessages = props.messagesData.messages.map(el => <Message message={el.message} key={el.id}/>)

    return (
        <div className={'dialogs_wrapper'} style={styleDialogsWrapper}>
            <div className={'dialogs'} style={styleDialogs}>
                {mappedDialogs}
            </div>
            <div className="messages">
                {mappedMessages}
            </div>
        </div>
    );
};

