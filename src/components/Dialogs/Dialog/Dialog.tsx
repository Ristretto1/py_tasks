import React from 'react';
import {NavLink} from "react-router-dom";

const styleDialogsItem = {
    padding: '5px'
}
const styleDialogsActive = {
    color: 'white'
}

type DialogPropsType = {
    name: string
    id: number
}
export const Dialog = (props: DialogPropsType) => {

    return (
        <div className={'dialogs_item'} style={styleDialogsItem}>
            <NavLink to={'/dialogs/'}>{props.name}</NavLink>
            {/*<NavLink to={`/dialogs/${props.id}`}>{props.name}</NavLink>*/}
        </div>
    );
};

