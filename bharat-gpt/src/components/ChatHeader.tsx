import React from 'react'

const ChatHeader = () => {
  return (
    <div className='flex flex-col items-center justify-start'>
      <p className='text-xs'>
        Chat with
      </p>
      <div className='flex gap-1.5 items-center justify-start'>
      <p className='h-2 w-2 bg-green-500 rounded-full' />
      <p className='text-md'>BharatGPT</p>
      </div>
    </div>
  )
}

export default ChatHeader