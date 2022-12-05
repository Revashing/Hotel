from django.urls import path
from .views import *


app_name = 'PGapp'

urlpatterns = [
	path('', start_page, name='start_page'),

	path('room_reserving', room_reserving, name='room_reserving'),
	path('add_room', add_room, name='add_room'),
	path('room_reserving/edit_room/<int:id>', edit_room, name='edit_room'),
	path('room_reserving/delete_room/<int:id>', delete_room, name='confirm_delete_room'),

	path('rubrics', rubrics, name='rubrics'),
	path('add_rubric', add_rubric, name='add_rubric'),
	path('rubrics/edit_rubric/<int:id>', edit_rubric, name='edit_rubric'),
	path('rubrics/delete_rubric/<int:id>', delete_rubric, name='confirm_delete_rubric'),

	path('employees', employees, name='employees'),
	path('add_employee', add_employee, name='add_employee'),
	path('employees/edit_employee/<int:id>', edit_employee, name='edit_employee'),
	path('employees/delete_employee/<int:id>', delete_employee, name='confirm_delete_employee'),

	path('hotel_rooms', hotel_rooms, name='hotel_rooms'),
	path('add_hotel_room', add_hotel_room, name='add_hotel_room'),
	path('hotel_rooms/edit_hotel_room/<int:hotel_room_id>', edit_hotel_room, name='edit_hotel_room'),
	path('hotel_rooms/delete_hotel_room/<int:hotel_room_id>', delete_hotel_room, name='confirm_delete_hotel_room'),
	path('hotel_rooms/room_full_view/<int:hotel_room_id>', room_full_view, name='room_full_view'),
	]