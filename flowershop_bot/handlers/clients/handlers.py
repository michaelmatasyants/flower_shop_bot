from telegram import Update
from telegram.ext import ConversationHandler, CallbackContext

from flowershop_bot.handlers.clients import texts
from flowershop_bot.models import User
from flowershop_bot.handlers.clients.keyboard import (make_keyboard_for_start_command)


def command_start(update: Update, context):
    print('command_start')
    if update.message:
        user_info = update.message.from_user.to_dict()
    else:
        user_info = {}
        user_info['id'] = context.user_data['user_id']
        user_info['first_name'] = context.user_data['first_name']
        #user_info['username'] = context.user_data['username']
    created = User.objects.get_or_create(tg_id=user_info['id'],)


    #args = context.args
    #if args:
    #    link_id = args[0]
    #    try:
    #        invitation_link = InvitationLink.objects.get(link_id=link_id)
    #        invitation_link.click_count += 1
    #        invitation_link.save()
    #    except InvitationLink.DoesNotExist:
    #        pass

    if created:
        text = texts.start_created.format(
            first_name=user_info['first_name']
        )
    else:
        text = texts.start_not_created.format(
            first_name=user_info['first_name']
        )

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text,
        reply_markup=make_keyboard_for_start_command(),
    )


def command_cancel(update: Update, _):
    print('command_cancel')
    text = texts.cancel_text
    update.message.reply_text(
        text=text,
        reply_markup=make_keyboard_for_start_command(),
    )
    return ConversationHandler.END