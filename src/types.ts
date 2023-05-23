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

export type StateType = {
    profileData: {
        posts: PostType[]
    }
    messagesData: {
        messages: MessageType[]
        dialogs: DialogType[]
    }
}