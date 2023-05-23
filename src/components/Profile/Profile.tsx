import React from 'react';
import {Posts} from "./Posts/Posts";
import {ProfileInfo} from "./ProfileInfo/ProfileInfo";
import {PostType} from "../../types";

type ProfilePropsType = {
    profileData: {
        posts: PostType[]
    }
}

export const Profile = (props: ProfilePropsType) => {
    return (
        <div>
            <ProfileInfo/>
            <Posts posts={props.profileData.posts}/>
        </div>
    );
}