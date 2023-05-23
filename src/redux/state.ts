import {DialogType, MessageType, PostType, StateType} from "../types";

export const state: StateType = {
    profileData: {
        posts:  [
            {id: 1, text: 'kirill', likesCount: 12},
            {id: 2, text: 'Anya', likesCount: 10},
            {id: 3, text: 'Tayson', likesCount: 8},
        ]
    },
    messagesData: {
        messages:  [
            {id: 1, message: '159'},
            {id: 2, message: '1jhjh59'},
            {id: 3, message: '4654oip'},
        ],
        dialogs: [
            {id: 1, name: 'Kirill'},
            {id: 2, name: 'Tayson'},
            {id: 3, name: 'Anya'},
        ]
    }
}