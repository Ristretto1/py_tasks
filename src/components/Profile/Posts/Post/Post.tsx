import React from 'react';

type PostPropsType = {
    text: string
}

export const Post = (props: PostPropsType) => {
    return (
        <div>
            {props.text}
        </div>
    );
};

