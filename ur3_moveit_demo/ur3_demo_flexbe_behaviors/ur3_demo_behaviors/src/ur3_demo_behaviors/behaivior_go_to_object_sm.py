#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_manipulation_states.moveit_to_joints_dyn_state import MoveitToJointsDynState
from flexbe_states.wait_state import WaitState
from miscellaneous_flexbe_states.get_tf_transform_state import GetTFTransformState
from miscellaneous_flexbe_states.message_state import MessageState
from moveit_flexbe_states.ik_get_joints_from_pose_state import IkGetJointsFromPose as moveit_flexbe_states__IkGetJointsFromPose
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on December 12, 2021
@author: Gerard Harkema
'''
class behaivior_go_to_objectSM(Behavior):
	'''
	Demo of a behavior using moveit for the open-manipulator robot
	'''


	def __init__(self):
		super(behaivior_go_to_objectSM, self).__init__()
		self.name = 'behaivior_go_to_object'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		action_topic = "move_group"
		arm_group = 'arm'
		# x:83 y:390, x:583 y:190
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['frames'])
		_state_machine.userdata.grasp_offset = 0.00
		_state_machine.userdata.rotation = 1.57
		_state_machine.userdata.move_group_prefix = ''
		_state_machine.userdata.tool_link = "tcp_link"
		_state_machine.userdata.frames = []
		_state_machine.userdata.group_name = 'arm'
		_state_machine.userdata.pre_grasp_offset = 0.03

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:73 y:24
			OperatableStateMachine.add('get_pose_transform',
										GetTFTransformState(),
										transitions={'done': 'pose_message', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'frames': 'frames', 'transform': 'part_pose'})

			# x:876 y:224
			OperatableStateMachine.add('go_grasp',
										MoveitToJointsDynState(move_group=arm_group, action_topic=action_topic),
										transitions={'reached': 'ik_calculate_post_grasp_pose', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:476 y:374
			OperatableStateMachine.add('go_post_grasp',
										MoveitToJointsDynState(move_group=arm_group, action_topic=action_topic),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:676 y:24
			OperatableStateMachine.add('go_pre_grasp',
										MoveitToJointsDynState(move_group=arm_group, action_topic=action_topic),
										transitions={'reached': 'wiat_pre_grasp', 'planning_failed': 'failed', 'control_failed': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:877 y:124
			OperatableStateMachine.add('ik_calculate_grasp_pose',
										moveit_flexbe_states__IkGetJointsFromPose(time_out=5.0, ignore_orientation=True),
										transitions={'continue': 'go_grasp', 'failed': 'failed', 'time_out': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'time_out': Autonomy.Off},
										remapping={'group_name': 'group_name', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link', 'pose': 'part_pose', 'offset': 'grasp_offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:664 y:374
			OperatableStateMachine.add('ik_calculate_post_grasp_pose',
										moveit_flexbe_states__IkGetJointsFromPose(time_out=5.0, ignore_orientation=True),
										transitions={'continue': 'go_post_grasp', 'failed': 'failed', 'time_out': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'time_out': Autonomy.Off},
										remapping={'group_name': 'group_name', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link', 'pose': 'part_pose', 'offset': 'pre_grasp_offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:467 y:24
			OperatableStateMachine.add('ik_calculate_pre_grasp_pose',
										moveit_flexbe_states__IkGetJointsFromPose(time_out=5.0, ignore_orientation=True),
										transitions={'continue': 'go_pre_grasp', 'failed': 'failed', 'time_out': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'time_out': Autonomy.Off},
										remapping={'group_name': 'group_name', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link', 'pose': 'part_pose', 'offset': 'pre_grasp_offset', 'rotation': 'rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:273 y:24
			OperatableStateMachine.add('pose_message',
										MessageState(severity=Logger.REPORT_HINT, header="Pose of testpoint"),
										transitions={'continue': 'ik_calculate_pre_grasp_pose'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'part_pose'})

			# x:899 y:24
			OperatableStateMachine.add('wiat_pre_grasp',
										WaitState(wait_time=2),
										transitions={'done': 'ik_calculate_grasp_pose'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
