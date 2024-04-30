"use client";

import React from "react";
import PropTypes from "prop-types";
import TextareaAutomsize from "react-textarea-autosize";

const ChatInput = (
  props: React.JSX.IntrinsicAttributes &
    React.ClassAttributes<HTMLDivElement> &
    React.HTMLAttributes<HTMLDivElement>
) => {
  return (
    <div {...props} className="border-t border-zinc-300">
      <div className="relative mt-4 flex-1 overflow-hidden rounded-lg border-none outline-none">
        <TextareaAutomsize
          rows={2}
          maxRows={4}
          autoFocus
          placeholder="Message..."
          className="peer disabled:opacity-50 pr-14 resize-none block w-full border-0 bg-zinc-100 py-1.5 text-gray-900 focus:ring-0"
        />
      </div>
    </div>
  );
};

ChatInput.propTypes = {};

export default ChatInput;
