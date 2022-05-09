#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from avans_vacuum_gripper_flexbe_states.vacuum_gripper_control_state import VacuumGripperControlState
from flexbe_states.wait_state import WaitState
from miscellaneous_flexbe_states.select_state import SelectState
from miscellaneous_flexbe_states.tf_transform_state import TFTransformState
from open_manipulator_moveit_flexbe_states.srdf_state_to_moveit import SrdfStateToMoveit as open_manipulator_moveit_flexbe_states__SrdfStateToMoveit
from pcl_flexbe_states.pcl_calculate_object_pose_state import PclCalculateObjectPoseState
from ur3_demo_behaviors.behaivior_go_to_object_sm import behaivior_go_to_objectSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on December 12, 2021
@author: Gerard Harkema
'''
class pick_n_placeSM(Behavior):
	'''
	Demo of a behavior using moveit for the open-manipulator robot
	'''


	def __init__(self):
		super(pick_n_placeSM, self).__init__()
		self.name = 'pick_n_place'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(behaivior_go_to_objectSM, 'behaivior_go_to_object')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		arm_group = 'arm'
		action_topic = "move_group"
		# x:33 y:340, x:632 y:336
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.move_group_prefix = ''
		_state_machine.userdata.move_group = "move_group"
		_state_machine.userdata.ee_link = "end_effector_link"
		_state_machine.userdata.frames = ["world" , "object_to_grasp_world"]
		_state_machine.userdata.use_vacuum_gripper = True
		_state_machine.userdata.object_to_grasp = 'object_to_grasp'
		_state_machine.userdata.object_to_grasp_world = 'object_to_grasp_world'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:47 y:24
			OperatableStateMachine.add('go_home',
										open_manipulator_moveit_flexbe_states__SrdfStateToMoveit(config_name='home', move_group=arm_group, action_topic=action_topic, robot_name="", tolerance=0.0),
										transitions={'reached': 'go_photo', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:322 y:574
			OperatableStateMachine.add('dummy_wait_vacuumo_off',
										WaitState(wait_time=2.0),
										transitions={'done': 'go_resting'},
										autonomy={'done': Autonomy.Off})

			# x:1073 y:124
			OperatableStateMachine.add('dummy_wait_vacuumo_on',
										WaitState(wait_time=2.0),
										transitions={'done': 'behaivior_go_to_object'},
										autonomy={'done': Autonomy.Off})

			# x:747 y:574
			OperatableStateMachine.add('go_drop',
										open_manipulator_moveit_flexbe_states__SrdfStateToMoveit(config_name='drop', move_group=arm_group, action_topic=action_topic, robot_name="", tolerance=0.0),
										transitions={'reached': 'select_vaccum_gripper_2', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:297 y:24
			OperatableStateMachine.add('go_photo',
										open_manipulator_moveit_flexbe_states__SrdfStateToMoveit(config_name='photo', move_group=arm_group, action_topic=action_topic, robot_name="", tolerance=0.0),
										transitions={'reached': 'take_pcl_photo', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:47 y:574
			OperatableStateMachine.add('go_resting',
										open_manipulator_moveit_flexbe_states__SrdfStateToMoveit(config_name='resting', move_group=arm_group, action_topic=action_topic, robot_name="", tolerance=0.0),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1047 y:574
			OperatableStateMachine.add('post_pick',
										open_manipulator_moveit_flexbe_states__SrdfStateToMoveit(config_name='pre_post_pick', move_group=arm_group, action_topic=action_topic, robot_name="", tolerance=0.0),
										transitions={'reached': 'go_drop', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:797 y:24
			OperatableStateMachine.add('pre_pick',
										open_manipulator_moveit_flexbe_states__SrdfStateToMoveit(config_name='pre_post_pick', move_group=arm_group, action_topic=action_topic, robot_name="", tolerance=0.0),
										transitions={'reached': 'select_vaccum_gripper_1', 'planning_failed': 'failed', 'control_failed': 'failed', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name', 'move_group': 'move_group', 'robot_name': 'robot_name', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1073 y:24
			OperatableStateMachine.add('select_vaccum_gripper_1',
										SelectState(),
										transitions={'true': 'turn_vacuum_on', 'false': 'dummy_wait_vacuumo_on'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'select': 'use_vacuum_gripper'})

			# x:523 y:574
			OperatableStateMachine.add('select_vaccum_gripper_2',
										SelectState(),
										transitions={'true': 'turn_vacuum_off', 'false': 'dummy_wait_vacuumo_off'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'select': 'use_vacuum_gripper'})

			# x:571 y:24
			OperatableStateMachine.add('take_pcl_photo',
										PclCalculateObjectPoseState(),
										transitions={'continue': 'transform_pose', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:840 y:184
			OperatableStateMachine.add('transform_pose',
										TFTransformState(new_frame_id='world'),
										transitions={'done': 'pre_pick', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_pose': 'object_to_grasp', 'transformd_pose': 'object_to_grasp_world'})

			# x:302 y:674
			OperatableStateMachine.add('turn_vacuum_off',
										VacuumGripperControlState(gripper_vacuum_enable=False, target_time=1.0),
										transitions={'done': 'go_resting'},
										autonomy={'done': Autonomy.Off})

			# x:1302 y:24
			OperatableStateMachine.add('turn_vacuum_on',
										VacuumGripperControlState(gripper_vacuum_enable=True, target_time=1.0),
										transitions={'done': 'behaivior_go_to_object'},
										autonomy={'done': Autonomy.Off})

			# x:1318 y:321
			OperatableStateMachine.add('behaivior_go_to_object',
										self.use_behavior(behaivior_go_to_objectSM, 'behaivior_go_to_object'),
										transitions={'finished': 'post_pick', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'frames': 'frames'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
