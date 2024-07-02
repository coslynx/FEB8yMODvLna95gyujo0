const openAI = require('ai-chatbot');

function contentModeration(content) {
    return openAI.detectContent(content);
}

module.exports = {
    contentModeration,
};