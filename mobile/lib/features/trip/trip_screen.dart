import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

class TripScreen extends ConsumerStatefulWidget {
  const TripScreen({super.key});

  @override
  ConsumerState<TripScreen> createState() => _TripScreenState();
}

class _TripScreenState extends ConsumerState<TripScreen> {
  // Mock state for now
  String _status = "IDLE";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("RideFlow Map")),
      body: Stack(
        children: [
          const Center(
            child: Text("Map Placeholder (OpenStreetMap goes here)"),
          ),
          if (_status != "IDLE")
            Positioned(
              bottom: 0,
              left: 0,
              right: 0,
              child: Card(
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text("Status: $_status"),
                      const LinearProgressIndicator(),
                    ],
                  ),
                ),
              ),
            ),
          Positioned(
            bottom: 24,
            left: 24,
            right: 24,
            child: ElevatedButton(
              onPressed: () {
                setState(() => _status = "SEARCHING");
                // Call API logic later
              },
              child: const Text("Request Ride"),
            ),
          ),
        ],
      ),
    );
  }
}
