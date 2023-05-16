import React from 'react';

const styleProfileBackground = {
    height: '150px',
    width: '100%',
}
export const ProfileInfo = () => {
    return (
        <div style={{marginBottom: '30px'}}>
            <div>
                <img style={styleProfileBackground}
                     src="https://mobimg.b-cdn.net/v3/fetch/47/47bf7e2bdbbc5da720db314f8bc62ce8.jpeg?w=1470&r=0.5625"/>
            </div>
            <div>
                ava + desc
            </div>
        </div>
    );
};

