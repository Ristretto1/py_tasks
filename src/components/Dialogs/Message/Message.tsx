import React from 'react';

const styleMessagesItem = {
    padding: '5px'
}

type MessagePropsType = {
    message: string
}
export const Message = (props: MessagePropsType) => {
    return (
        <div className="messages_item" style={styleMessagesItem}>{props.message}</div>
    );
};

