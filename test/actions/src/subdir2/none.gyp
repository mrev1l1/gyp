{
  'targets': [
    {
      'target_name': 'file',
      'type': 'none',
      'msvs_cygwin_shell': 0,
      'actions': [
        {
          'action_name': 'make-file',
          'inputs': [
            'make-file.py',
          ],
          'outputs': [
            'file.out',
            # TODO:  enhance testing infrastructure to test this
            # without having to hard-code the intermediate dir paths.
            #'<(INTERMEDIATE_DIR)/file.out',
          ],
          'action': [
            'python', '<(_inputs)', '<@(_outputs)',
          ],
          'process_outputs_as_sources': 1,
        }
      ],
    },
  ],
}
