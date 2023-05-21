import React from 'react';
import {Dialog} from "./Dialog/Dialog";
import {Message} from "./Message/Message";
import {DialogType, MessageType} from "../../index";

type DialogsPropsType = {
    dialogs: DialogType[]
    messages: MessageType[]
}

export const Dialogs = (props: DialogsPropsType) => {

    const styleDialogsWrapper = {
        display: 'flex'
    }
    const styleDialogs = {
        width: '150px'
    }

    return (
        <div className={'dialogs_wrapper'} style={styleDialogsWrapper}>
            <div className={'dialogs'} style={styleDialogs}>
                {props.dialogs.map(el => <Dialog name={el.name} id={el.id} key={el.id}/>)}

            </div>
            <div className="messages">
                {props.messages.map(el => <Message message={el.message} key={el.id}/>)}
            </div>
        </div>
    );
};

